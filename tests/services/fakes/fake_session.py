class FakeSession:

    should_commit_fail = True

    def commit(self):
        if self.should_commit_fail:
            raise Exception("Commit failed")

        print("commit called")

    def rollback(self):
        print("rollback called")
        pass